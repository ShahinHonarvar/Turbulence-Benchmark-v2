def palindrome_of_length_n(s):
    list(filter(lambda x: x == x[::-1], s.lower()))