def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[:7].lower()
    letters = ''.join(sorted(s))
    ret = set()
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            if is_palindrome(letters[i:j]):
                ret.add(letters[i:j])
    return ret