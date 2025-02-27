def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = [char for char in s if char.isalpha()]
    if len(letters) < 2:
        return set()
    result = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for arrangement in itertools.permutations(letters[i:i + length]):
                if arrangement == arrangement[::-1]:
                    palindrome = ''.join(arrangement)
                    result.add(palindrome)
    return result