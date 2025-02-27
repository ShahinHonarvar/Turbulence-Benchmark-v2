def return_vowels(a):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(37, 57):
        if a[i] in vowels and a[i] > '*' and (a[i] <= 'P') and (result.count(a[i]) == 0):
            result.append(a[i])
    return result