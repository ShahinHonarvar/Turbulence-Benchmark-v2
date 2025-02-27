def palindromes_between_indices(input_string):
    substring = input_string[8:10]
    palindromes_set = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            palindrome = substring[i:j]
            if palindrome == palindrome[::-1].lower():
                palindromes_set.add(palindrome)
    return palindromes_set