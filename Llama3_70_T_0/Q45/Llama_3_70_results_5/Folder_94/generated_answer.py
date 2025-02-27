def palindromes_between_indices(s):
    s = s[3:5].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for j in range(len(s) - i + 1):
            substr = s[j:j + i]
            for k in range(len(substr)):
                for m in range(k + 1, len(substr) + 1):
                    first_half = substr[k:m]
                    second_half = first_half[::-1]
                    palindrome = first_half + second_half
                    if len(palindrome) >= 3:
                        palindromes.add(palindrome)
    return palindromes