import itertools

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[6:10])).lower()
    letters = set(substring)
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(5, len(substring) + 1):
        for combination in itertools.combinations_with_replacement(letters, length // 2):
            palindrome = ''.join(combination + combination[-(length // 2 + length % 2):-1 if length % 2 else -length // 2][::-1])
            palindromes.add(palindrome)
    return palindromes