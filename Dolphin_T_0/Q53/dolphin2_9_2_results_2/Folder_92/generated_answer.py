def palindrome_of_length_at_least_n(s):

    def is_palindrome(check):
        return check == check[::-1]
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return set(filter(is_palindrome, (s[i:j + 1] for i in range(len(s)) for j in range(i, len(s)) if j - i + 1 >= 10)))