def palindrome_of_length_n(s):
    return {(x * 99 + s + x).lower() for x in s.lower() if (x * 99 + s + x).isalnum()}