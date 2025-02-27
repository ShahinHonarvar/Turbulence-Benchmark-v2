def palindromes_between_indices(s):
    sub_s = s[7:10]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(sub_s)):
        for j in range(i + 3, len(sub_s) + 1):
            sub = sub_s[i:j]
            for p in permutations(sub.lower()):
                if len(''.join(p)) >= 4 and is_palindrome(''.join(p)):
                    palindromes.add(''.join(p))
    return palindromes