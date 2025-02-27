def palindrome_of_length_n(s):
    palindrome = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            first_half = s[i:j + 1]
            second_half = first_half[::-1]
            if first_half.lower() == second_half.lower():
                palindrome.add(first_half)
    return palindrome