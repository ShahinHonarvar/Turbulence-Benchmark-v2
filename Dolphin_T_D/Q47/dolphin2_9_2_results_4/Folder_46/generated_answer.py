def palindromes_of_specific_lengths(s):
    substring = s[11:98]
    output = set()
    for length in range(29, 63):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            lower_sub = sub.lower()
            if lower_sub == lower_sub[::-1] and all((c in 'abcdefghijklmnopqrstuvwxyz' for c in sub)):
                output.add(sub)
    return output