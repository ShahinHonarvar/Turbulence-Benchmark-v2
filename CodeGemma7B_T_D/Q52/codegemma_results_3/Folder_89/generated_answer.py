def palindrome_of_length_n(str):

    def create_palindrome(l):
        if len(l) == n:
            palindromes.add(''.join(l))
        for k in range(len(s)):
            if s[k].isalpha():
                l.append(s[k])
                create_palindrome(l)
                l.pop()
    try:
        n = 37
        s = str.lower()
        palindromes = set()
        create_palindrome([])
        return palindromes
    except:
        return set()