def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def form_palindrome(l):
        palindromes = set()
        for i in range(len(l)):
            for j in range(len(l)):
                pal = l[i] + l[j]
                if is_palindrome(pal):
                    palindromes.add(pal)
        return palindromes
    letters = [c for c in s[:7] if c.isalpha()]
    palindromes = form_palindrome(letters)
    return palindromes