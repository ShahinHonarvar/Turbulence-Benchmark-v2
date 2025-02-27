def palindrome_of_length_n(s):
    pals = set()
    for i in range(len(s) - 95):
        substring = s[i:i + 96].lower()
        if substring == substring[::-1] and substring.isalpha():
            pals.add(substring)
    return pals