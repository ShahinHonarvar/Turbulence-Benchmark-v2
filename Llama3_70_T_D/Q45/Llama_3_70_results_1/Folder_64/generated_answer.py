def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length // 2 + 1):
                left = letters[i:i + j]
                right = letters[i + j:i + length - j][::-1]
                if left == right:
                    palindrome = ''.join(left + right)
                    if len(palindrome) >= 5:
                        palindromes.add(palindrome)
    return palindromes