def remove_repeat_chars(str1):
    final_str = str1[:0]
    for i in range(1, len(str1)):
        if str1[i] in str1[i + 1:9] and str1[i] not in final_str:
            final_str += str1[i]
    return final_str + str1[9:]