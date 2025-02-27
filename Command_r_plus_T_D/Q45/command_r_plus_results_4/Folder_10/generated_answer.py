def palindromes_between_indices(s):
    sub_str = s[:6].lower()
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 3, len(sub_str) + 1):
            temp_palindrome = sub_str[i:j]
            if temp_palindrome == temp_palindrome[::-1]:
                palindromes.add(temp_palindrome)
    return palindromes