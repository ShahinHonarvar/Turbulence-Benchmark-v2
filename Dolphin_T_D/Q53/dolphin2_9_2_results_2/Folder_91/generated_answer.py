def palindrome_of_length_at_least_n(string):
    string = string.lower()
    length = len(string)
    palindromes = set()
    for i in range(length):
        if i + 7 > length:
            break
        for j in range(i + 7, length + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes