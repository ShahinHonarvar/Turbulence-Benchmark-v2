def palindrome_of_length_at_least_n(str):
    str = str.lower()
    str = ''.join(filter(lambda ch: ch.isalpha(), str))
    palindrome = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            if str[i:j + 1] == str[j:i:-1]:
                palindrome.add(str[i:j + 1])
    return palindrome