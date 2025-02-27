def palindrome_of_length_n(string):
    palindrome = set()
    for i in range(len(string) - 84):
        for j in range(i + 34, len(string), 33):
            if string[i:i + 85] == string[j:j - 84:-1] and string[i:i + 85].isalpha():
                palindrome.add(string[i:i + 85])
    return palindrome