def palindromes_of_specific_lengths(text):
    sub_str = text[15:73]
    palindromes = set()
    for index in range(len(sub_str)):
        for length in range(19, 56):
            if index + length <= len(sub_str) and sub_str[index:index + length] == sub_str[index:index + length][::-1]:
                palindrome = sub_str[index:index + length].lower()
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes