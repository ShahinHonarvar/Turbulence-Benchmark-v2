def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    substring = input_string[5:8].lower()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            palindrome = substring[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes