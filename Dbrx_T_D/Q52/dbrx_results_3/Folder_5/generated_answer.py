def palindrome_of_length_n(text):
    result_set = set()
    n = 17
    if len(text) < n:
        return result_set
    for i in range(len(text) - n + 1):
        palindrome = text[i:i + n]
        if palindrome.lower() == palindrome.lower()[::-1] and palindrome.isalpha():
            result_set.add(palindrome)
    return result_set