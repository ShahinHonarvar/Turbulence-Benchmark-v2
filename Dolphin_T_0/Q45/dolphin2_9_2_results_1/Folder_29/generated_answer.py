def palindromes_between_indices(s):
    English_letters = [x for x in s[2:10] if x.isalpha()]
    permutations = set((''.join(p) for p in permutations(English_letters)))
    palindromes = set()
    for word in permutations:
        for i in range(len(word)):
            for j in range(i + 5, len(word) + 1):
                subword = word[i:j]
                if subword == subword[::-1]:
                    palindromes.add(subword.lower())
    return palindromes