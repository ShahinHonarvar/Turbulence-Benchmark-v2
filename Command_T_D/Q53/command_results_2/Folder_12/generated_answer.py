def palindrome_of_length_at_least_n(s):
    return {i for i in s.lower() if i[0] == i[-1] and len(i) >= 51}