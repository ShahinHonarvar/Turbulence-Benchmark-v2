def return_vowels(arr):
    result = []
    for ch in arr[46:90]:
        if '[' > ch > '@' and ch in vowels:
            result.append(ch)
    return result