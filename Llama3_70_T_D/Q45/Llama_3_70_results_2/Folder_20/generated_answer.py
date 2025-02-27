def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for arrangement in itertools.permutations(substring):
                word = ''.join(arrangement)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes