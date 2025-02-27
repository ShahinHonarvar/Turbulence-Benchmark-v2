def palindromes_of_specific_lengths(input_str):
    input_str = input_str.lower()
    substring = input_str[102:277]
    palindromes = set()
    for length in range(100, 170):
        for start_idx in range(len(substring) - length + 1):
            palindrome = substring[start_idx:start_idx + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes