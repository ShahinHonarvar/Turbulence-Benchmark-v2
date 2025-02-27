def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:8] if c.isalpha()]
    if len(letters) < 3:
        return set()
    possible_palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters)):
            if letters[i] == letters[j]:
                possible_palindromes.add(''.join(letters[i:j + 1]))
    return possible_palindromes