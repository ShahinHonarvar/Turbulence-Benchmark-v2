def palindromes_of_specific_lengths(input_str):
    palindrome_set = set()
    input_str = input_str.lower()
    for i in range(0, 7):
        for j in range(i + 3, 7):
            substring = input_str[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    if not palindrome_set:
        return set()
    return palindrome_set