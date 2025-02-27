def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for arrangement in generate_arrangements(letters[i:i + length]):
                palindrome = arrangement + arrangement[:-1][::-1]
                if len(palindrome) >= 6:
                    palindromes.add(palindrome)
    return palindromes

def generate_arrangements(letters):
    if len(letters) == 1:
        yield letters
    else:
        for i, letter in enumerate(letters):
            remaining_letters = letters[:i] + letters[i + 1:]
            for arrangement in generate_arrangements(remaining_letters):
                yield (letter + arrangement)