def palindrome_of_length_n(s):
    substrings = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - 84):
        substring = s[i:i + 85]
        if substring == substring[::-1]:
            substrings.add(substring)
    return substrings