def remove_repeat_chars(str1):
    final_string = ''
    for i in range(len(str1)):
        if i < 46 or i > 91:
            final_string += str1[i]
        else:
            while i < len(str1) and str1[i] in final_string:
                i += 1
            final_string += str1[i]
    return final_string