def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def generate_palindromes(word):
        palindromes = set()
        if len(word) < 5:
            return palindromes

        def backtrack(start, end):
            if start > end:
                palindrome = ''.join(word[start:end + 1])
                if is_palindrome(palindrome):
                    palindromes.add(palindrome)
                return
            for i in range(start, end + 1):
                word[start], word[i] = (word[i], word[start])
                backtrack(start + 1, end)
                word[start], word[i] = (word[i], word[start])
        backtrack(0, len(word) - 1)
        return palindromes
    s = s[3:9].replace(' ', '').lower()
    return generate_palindromes(list(s))