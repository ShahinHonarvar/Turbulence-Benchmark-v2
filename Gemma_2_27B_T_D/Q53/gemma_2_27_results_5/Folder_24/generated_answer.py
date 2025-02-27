def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s) - 52):
        substring = s[i:i + 53].lower()
        if substring == substring[::-1]:
            result.add(s[i:i + 53])
    return result