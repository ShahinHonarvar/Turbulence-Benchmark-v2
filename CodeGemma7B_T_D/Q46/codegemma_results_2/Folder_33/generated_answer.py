def gcf_three_nums(nums):
    two_hun_fif_two = nums[252]
    hun_for_nine = nums[149]
    five_six_four = nums[564]
    four = 4
    while two_hun_fif_two % four != 0:
        two_hun_fif_two -= 1
        hun_for_nine -= 1
        five_six_four -= 1
    while hun_for_nine % four != 0:
        hun_for_nine -= 1
        five_six_four -= 1
    while five_six_four % four != 0:
        five_six_four -= 1
    return two_hun_fif_two