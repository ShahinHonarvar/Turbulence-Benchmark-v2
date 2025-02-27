def form_palindromes(pattern):
    if len(pattern) < 3:
        return {pattern}
    palindromes = set()
    for i in range(len(pattern) // 2 + 1 if len(pattern) % 2 == 1 else 0):
        palindrome = pattern[:i] + pattern[::-1][i:]
        palindromes.add(palindrome)
        palindromes.update(form_palindromes(palindrome[1:-1]))
    return palindromes

def palindromes_between_indices(s):
    pattern = ''.join(sorted(set(s[5:8].lower()) & set('abcdefghijklmnopqrstuvwxyz')))
    return form_palindromes(pattern)