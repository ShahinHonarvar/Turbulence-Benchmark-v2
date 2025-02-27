def palindromes_between_indices(s):
    s_low = s.lower()
    chars = [c for c in s_low[:4] if c.isalpha()]
    palindromes = set()
    for i in range(len(chars)):
        for j in range(i + 1, len(chars) + 1):
            first_part = ''.join(chars[i:j])
            for k in range(len(chars)):
                for end in range(k + 1, len(chars) + 1):
                    second_part = ''.join(chars[k:end])
                    palindrome = first_part + second_part[::-1]
                    if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes