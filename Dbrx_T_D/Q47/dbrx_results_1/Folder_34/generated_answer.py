def palindromes_of_specific_lengths(input_string):
    sub_string = input_string[200:301].lower()
    palindromes = {palindrome for i in range(10, 51) for palindrome in {sub_string[i:j] for j in range(i + 1, len(sub_string) - i + 1)} if palindrome == palindrome[::-1] and palindrome.isalpha()}
    return palindromes