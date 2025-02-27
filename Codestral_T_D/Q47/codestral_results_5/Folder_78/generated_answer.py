def palindromes_of_specific_lengths(s):
    s = s[15:73].lower()
    alpha = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for l in range(19, 56):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub == sub[::-1] and set(sub) <= alpha:
                result.add(sub)
    return result