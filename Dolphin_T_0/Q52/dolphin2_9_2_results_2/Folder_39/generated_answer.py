def palindrome_of_length_n(s):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s) - 58):
        sub = s[i:i + 59]
        is_palindrome = True
        for j in range(len(sub) // 2):
            if sub[j].lower() not in chars or sub[~j].lower() not in chars:
                is_palindrome = False
                break
            if sub[j].lower() != sub[~j].lower():
                is_palindrome = False
                break
        if is_palindrome:
            palindromes.add(sub)
    return palindromes