def palindrome_of_length_n(str):
    palindrome_set = set()
    palindrome_set.update([str[i:i + 257] for i in range(len(str) - 256)])
    return palindrome_set