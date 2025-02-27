def palindromes_between_indices(s):
    sub_string = s[3:10]
    unique_letters = set(sub_string.lower()) - {''}
    return {''.join(i) for i in unique_letters.__pow__(2, length=len(sub_string)) if i == i[::-1]}