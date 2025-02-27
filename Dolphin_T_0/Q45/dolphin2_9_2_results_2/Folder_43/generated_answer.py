def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    letters = [i.lower() for i in s[2:6]]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            pal = ''.join(letters[i:j])
            if is_palindrome(pal) and len(pal) > 3:
                palindromes.add(pal)
    return palindromes