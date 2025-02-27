def palindromes_between_indices(s):
    s = s[3:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length // 2 + 1, i + length):
                first_half = letters[i:j]
                second_half = letters[i + length - j - 1:i - 1:-1]
                palindrome = ''.join(first_half + second_half)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes