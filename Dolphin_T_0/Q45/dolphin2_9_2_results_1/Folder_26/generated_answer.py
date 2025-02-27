def palindromes_between_indices(s):
    l = ''.join(sorted(s[4:6])).lower()
    palindromes = set()

    def is_palindrome(word):
        word_l = len(word)
        if word_l < 3:
            return False
        return all((word[i] == word[word_l - i - 1] for i in range(word_l // 2)))
    for i in range(len(l)):
        for j in range(i + 2, len(l) + 1):
            for p in permutations(l[i:j]):
                if is_palindrome(''.join(p)):
                    palindromes.add(''.join(p))
    return palindromes