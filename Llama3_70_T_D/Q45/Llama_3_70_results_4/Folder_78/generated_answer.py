def palindromes_between_indices(s):
    s = s[6:9].lower()
    possible_palindromes = set()
    for i in range(3, len(s) + 1):
        for j in range(len(s) - i + 1):
            subs = s[j:j + i]
            subs = ''.join(sorted(subs))
            for k in range(len(subs) // 2, len(subs)):
                for p in range(k + 1):
                    palindrome = subs[p:k + 1] + subs[p:k][::-1]
                    if len(palindrome) >= 3:
                        possible_palindromes.add(palindrome)
    return possible_palindromes