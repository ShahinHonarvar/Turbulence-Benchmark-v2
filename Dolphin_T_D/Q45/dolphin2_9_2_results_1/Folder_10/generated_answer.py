import string

def palindromes_between_indices(s):
    letters = string.ascii_lowercase
    letters_in_range = {char.lower() for char in s[:6] if char.isalpha()}
    palindromes = set()
    for i in range(3, len(s[:6]) + 1):
        for subset in combinations(letters_in_range, i):
            for word in permutations(subset):
                word = ''.join(word)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes