def palindromes_between_indices(s):
    s = s[3:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    if len(letters) >= 2:
        for length in range(4, len(letters) + 1):
            for i in range(len(letters) - length + 1):
                first_half = letters[i:i + (length + 1) // 2]
                second_half = first_half[-2::-1] if length % 2 else first_half[::-1]
                palindrome = ''.join(first_half + second_half)
                palindromes.add(palindrome)
    return palindromes