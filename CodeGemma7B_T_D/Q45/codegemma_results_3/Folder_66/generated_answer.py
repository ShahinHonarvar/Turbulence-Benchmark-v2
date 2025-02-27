def palindromes_between_indices(txt_str):
    low, high = (0, 5)
    filtered_txt = [char for char in txt_str[low:high + 1] if char.isalpha()]
    filtered_txt = sorted(filtered_txt, key=str.lower)
    result = set()
    for i in range(len(filtered_txt)):
        for j in range(i, len(filtered_txt)):
            sub_str = ''.join(filtered_txt[i:j + 1])
            if sub_str == sub_str[::-1]:
                result.add(sub_str)
    if not result:
        return set()
    return result