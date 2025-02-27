def remove_repeat_chars(txt):
    final_str = ''
    for i, j in enumerate(txt):
        if i < 375 or i > 926 or j not in final_str:
            final_str += j
    return final_str