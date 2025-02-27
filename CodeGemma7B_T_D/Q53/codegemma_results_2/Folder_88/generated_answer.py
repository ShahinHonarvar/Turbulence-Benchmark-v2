def palindrome_of_length_at_least_n(str):
    str = str.lower()
    palindrome_dict = {}
    palindrome_set = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j] and j - i + 1 >= 27:
                palindrome_str = str[i:j + 1]
                if palindrome_str not in palindrome_dict:
                    palindrome_dict[palindrome_str] = palindrome_str
                    palindrome_set.add(palindrome_str)
    return palindrome_set