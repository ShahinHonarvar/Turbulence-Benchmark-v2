def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for p in get_palindromes(letters[i:i + length]):
                palindromes.add(''.join(p))
    return palindromes

def get_palindromes(letters):
    if len(letters) == 1:
        return [letters]
    elif len(letters) % 2 == 0:
        first_half = letters[:len(letters) // 2]
        second_half = letters[len(letters) // 2:]
        if first_half == second_half[::-1]:
            return [letters]
        else:
            return []
    else:
        first_half = letters[:len(letters) // 2]
        second_half = letters[len(letters) // 2 + 1:]
        if first_half == second_half[::-1]:
            middle = letters[len(letters) // 2]
            return [letters, middle + letters[1:][::-1]]
        else:
            return []