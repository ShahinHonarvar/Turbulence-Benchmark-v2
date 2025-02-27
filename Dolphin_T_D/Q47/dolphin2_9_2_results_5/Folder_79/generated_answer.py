def palindromes_of_specific_lengths(text):
    text = text[1:9]
    palindrome_set = set()
    for length in range(3, 5):
        for i in range(len(text) - length + 1):
            sub_string = text[i:i + length]
            if sub_string.lower() == sub_string.lower()[::-1] and sub_string.isalpha():
                palindrome_set.add(sub_string)
    return palindrome_set